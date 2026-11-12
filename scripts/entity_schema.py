#!/usr/bin/env python3
"""Build Organization + WebSite JSON-LD (with sameAs and founders) for GEO entity setup.

Example:
  python3 entity_schema.py --name "Acme Law" --url https://acmelaw.com \
    --description "Personal injury attorneys in Atlanta" \
    --same-as https://www.linkedin.com/company/acmelaw --same-as https://x.com/acmelaw \
    --founded 2009 --address "1 Peachtree St, Atlanta, GA 30303" --phone "+1-404-555-0100" \
    --founder "Jane Doe|https://www.linkedin.com/in/janedoe"
Paste the output in <head>, then check it at https://validator.schema.org/.
"""
import argparse, json, sys
from urllib.parse import urlparse


def _url(u):
    p = urlparse(u)
    if p.scheme not in ("http", "https") or not p.netloc:
        raise ValueError(f"not a full URL: {u!r}")
    return u


def build(name, url, description="", same_as=(), founded="", address="", phone="", founders=(), alternate_name=""):
    org = {"@type": "Organization", "@id": _url(url).rstrip("/") + "/#organization", "name": name, "url": url}
    if alternate_name: org["alternateName"] = alternate_name
    if description: org["description"] = description
    if same_as: org["sameAs"] = [_url(u) for u in same_as]
    if founded: org["foundingDate"] = founded
    if address: org["address"] = address  # ponytail: plain-text address; use PostalAddress fields if a validator asks
    if phone: org["telephone"] = phone
    people = []
    for f in founders:
        fname, _, link = f.partition("|")
        person = {"@type": "Person", "name": fname.strip()}
        if link.strip(): person["sameAs"] = [_url(link.strip())]
        people.append(person)
    if people: org["founder"] = people
    site = {"@type": "WebSite", "name": name, "url": url, "publisher": {"@id": org["@id"]}}
    if description: site["description"] = description
    return {"@context": "https://schema.org", "@graph": [org, site]}


def selftest():
    d = build("Acme", "https://acme.com/", "Widgets", ["https://x.com/acme"], "2009",
              founders=["Jane Doe|https://www.linkedin.com/in/jane", "Bob"])
    org, site = d["@graph"]
    assert org["@id"] == "https://acme.com/#organization" and site["publisher"]["@id"] == org["@id"]
    assert org["sameAs"] == ["https://x.com/acme"] and org["founder"][0]["sameAs"] == ["https://www.linkedin.com/in/jane"]
    assert "sameAs" not in org["founder"][1]
    try:
        build("Acme", "acme.com"); assert False, "bad URL accepted"
    except ValueError:
        pass
    print("selftest ok")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest(); sys.exit()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name", required=True)
    ap.add_argument("--url", required=True)
    ap.add_argument("--description", default="")
    ap.add_argument("--alternate-name", default="")
    ap.add_argument("--same-as", action="append", default=[], help="profile URL; repeat for each profile")
    ap.add_argument("--founded", default="")
    ap.add_argument("--address", default="")
    ap.add_argument("--phone", default="")
    ap.add_argument("--founder", action="append", default=[], help='"Name|https://linkedin.com/in/..."')
    a = ap.parse_args()
    try:
        data = build(a.name, a.url, a.description, a.same_as, a.founded, a.address, a.phone, a.founder, a.alternate_name)
    except ValueError as e:
        sys.exit(f"error: {e}")
    print('<script type="application/ld+json">\n' + json.dumps(data, indent=2) + "\n</script>")

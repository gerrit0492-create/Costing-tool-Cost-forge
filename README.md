# Cost-tool-pages — Final Pack (plug-and-play)

Dit pakket bevat:
- ✅ projectstructuur (pages/, utils/, data/, .streamlit/)
- ✅ werkende sanity-page: `pages/01_Calculatie.py`
- ✅ voorbeelddata (materials/processes/BOM)
- ✅ `.gitignore` + `requirements.txt`
- ✅ workflows: auto-unpack bij ZIP upload + handmatige Clean Sweep

## Gebruik
1) Maak (of open) je GitHub repo. Upload **deze ZIP** naar de root en commit naar `main`.
2) Maak **éénmalig** het workflow-bestand zichtbaar (als het nog niet bestaat): `.github/workflows/auto-unpack-clean.yml` (zit in de ZIP; zo nodig eerst los uploaden).
3) Upload volgende updates ook gewoon als ZIP → workflow pakt automatisch uit en commit.
4) Draai **Clean Sweep** vanuit Actions om resterende rommel weg te halen.

Start lokaal:
```
pip install -r requirements.txt
streamlit run home.py
```

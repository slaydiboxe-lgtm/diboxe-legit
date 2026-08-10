# DIBOXE LEGIT — Scammer Reports

The Scammers page now supports **multiple scammers and multiple evidence images per scammer**.

## Folder structure

Create one folder for each scammer:

```text
assets/scammers/
├── scammer-001/
│   ├── info.json
│   ├── profile.jpg
│   └── evidence/
│       ├── evidence-01.jpg
│       ├── evidence-02.png
│       └── evidence-03.jpg
│
└── scammer-002/
    ├── info.json
    ├── profile.png
    └── evidence/
        ├── evidence-01.jpg
        └── evidence-02.png
```

## `info.json`

Example:

```json
{
  "name": "John Doe",
  "username": "@example",
  "platform": "Facebook",
  "description": "Short description of the report.",
  "profile": "profile.jpg"
}
```

- `name`: name shown on the card.
- `username`: optional account/username.
- `platform`: optional platform.
- `description`: optional description.
- `profile`: the main image shown on the card. It must be inside the same scammer folder.

## Adding evidence

Put every screenshot/photo/evidence file inside that scammer's `evidence/` folder.

Supported image formats:

- `.jpg`
- `.jpeg`
- `.png`
- `.webp`
- `.gif`

You do **not** need to edit `scammers.html`.

## GitHub workflow

After you push the new files, the GitHub Action:

`.github/workflows/scammer-gallery.yml`

automatically rebuilds:

`assets/scammers/index.json`

The website then shows the scammer and all of their evidence in the gallery.

### Important

If you upload files to GitHub, wait for the **Update Scammer Gallery** GitHub Action to finish before checking the live website. Also hard-refresh the page if an old version is cached.

## Template

A blank example is included at:

`assets/scammers/scammer-001/`

Replace its `info.json` and add the real `profile.jpg` plus evidence files.

## Profile image fix

The gallery now automatically resolves profile and evidence image paths.
For each scammer, keep the profile image beside `info.json` and use:

`"profile": "profile.jpg"`

You do not need to write `assets/scammers/...` inside `info.json`.


## Professional gallery UI

The scammer reports page now includes a polished responsive layout, sticky navigation,
search, report/evidence statistics, improved cards, lazy-loaded profile images,
a refined evidence viewer, mobile optimization, and reduced-motion support.
The existing folder and `info.json` workflow remains unchanged.

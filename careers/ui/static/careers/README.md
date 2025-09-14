# UI Styles

Basic commands to get started.

First `cd` into dir:

```console
cd careers/ui/static/careers
```

To generate the styles:

```console
npm install
cd careers/ui/static/careers
npx @tailwindcss/cli -i ../static/careers/css/app.css -o ../static/careers/css/styles.css --cwd ../../templates -m -w
```

To format the templates:

```console
npx prettier -w ../../templates
```

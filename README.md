# Tailwindo.py


<p align="center">
  <img src="https://pbs.twimg.com/media/DQ-mDgSX0AUpCPL.png">
</p>

Python port of https://github.com/awssat/tailwindo

This tool can **convert your Bootstrap CSS classes** in HTML/JSX files to equivalent **Tailwind CSS** classes.

## Features

- Made to be easy to add more CSS frameworks in the future (currently Bootstrap).
- Can convert single files/code snippets/folders.
- Can extract changes to a separate css file as Tailwind components and keep old classes names. like: 

```
.p-md-5 {
	@apply md:p-7;
}
```



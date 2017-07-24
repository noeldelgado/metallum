# Metallum

[![npm-image](https://img.shields.io/npm/v/metallum.svg)](https://www.npmjs.com/package/metallum)
![license-image](https://img.shields.io/npm/l/metallum.svg)

Fetch lyrics from [metal-archives.com](https://www.metal-archives.com) using the command-line.

<img src="screenshot.gif" width="613">

## Install
Ensure you have [python](https://www.python.org/) installed.

### NPM

```sh
$ npm install --global metallum
```

### Manual Install

- Clone or download this repo.
- Create an alias on your `.zshrc` or `.bash_profile`:

	```sh
	alias met="python ~/<path-to-repo>/metallum.py"
	```

## Usage

```sh
~ met <band_name> <song_title>
```

### Example

```sh
~ met therion quetzalcoatl
```

That will search the song “quetzalcoatl” by the band “therion” and return the first coincidence. If not lyrics are found it will return “Lyrics not found”.

By default it will show the artist and song names before the lyrics. To only display the lyrics pass the `-t` or `--notitle` option.

### Arguments
```
usage: metallum.py [-h] [-t] band_name song_title

Fetch lyrics from http://metal-archives.com

positional arguments:
  band_name      The name of the band. e.g.: "Dark Reality"
  song_title     The title of the song. e.g.: "Mopin Carol"

optional arguments:
  -h, --help     show this help message and exit
  -t, --notitle  Don't show title.
```

### Don’t type the whole thing

Sometimes song titles (or even band names) are too long to type or even to remember them.

Let‘s put as an example the song ***“In an Excruciating Way Infested with Vermin and Violated by Executioners Who Practise Incendiarism and Desanctifying the Pious”*** by ***“Wormphlegm”*** ... well, you can get the lyrics by just typing:

```sh
met wormphlegm infested
```

Or the song ***“The Dark Liege Of Chaos Is Unleashed At The Ensorcelled Shrine Of A’Zura Kai (The Splendour Of A Thousand Swords Gleaming Beneath The Blazon Of The Hyperborean Empire Part II)”*** by ***“Bal-Sagoth”***

```sh
met balsagoth chaos
```

## License
MIT © [Noel Delgado](http://pixelia.me/)

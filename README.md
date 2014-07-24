# Metallum

Search and print out lyrics from http://metal-archives.com using the command-line.

![sample](https://raw.githubusercontent.com/noeldelgado/metallum/master/img/UrutianO2X.gif)

## Usage

```
python ~/<path-to-repo>/metallum.py <band_name> <song_title>
```

Additionally, you can create an alias on your `.zshrc` or `.bash_profile`:

```
alias metallum="python ~/<path-to-repo>/metallum.py"
" Or even shorter
alias met="python ~/<path-to-repo>/metallum.py"
```

So you can use it like: `met therion quetzalcoatl`

### You don't have to type the whole thing

Sometimes song titles (or even band names) are too long to type or even to remember them.

Let's put as an example the song ***"In an Excruciating Way Infested with Vermin and Violated by Executioners Who Practise Incendiarism and Desanctifying the Pious"*** by ***"Wormphlegm"***... well, you can get the lyrics by just typing:

`~ met wormphlegm infested`

Or the song ***"The Dark Liege Of Chaos Is Unleashed At The Ensorcelled Shrine Of A'Zura Kai (The Splendour Of A Thousand Swords Gleaming Beneath The Blazon Of The Hyperborean Empire Part II)"*** by ***"Bal-Sagoth"***

`~ met balsagoth chaos`

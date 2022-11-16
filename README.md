# words
use the python wikipedia api to get words that pertain to a certain subject. Good for building password list and natural language processing

## Installation

### Dependencies

  linux / macos

```bash
pip3 install wikipedia
```
  windows
  
```
pip install wikipedia
```
### Getting Started

```bash
git clone https://github.com/Donny-GUI/words.git
cd words
python3 setup.py
python3 setup_cmdline_tool.py
words about "Dolphins"

```


## File Structure

Pretty straight forward filestructure, prevents harsh loading times for long word lists.

### ./words/ directory

![struct1](https://user-images.githubusercontent.com/108424001/202072486-e9fcbc5c-ac31-47d2-8a9c-180d562cb6fc.png)

### ./words/a/

![file2](https://user-images.githubusercontent.com/108424001/202072662-dc18ed2b-45af-4f35-8221-07f691cf3d30.png)


## Creating the File Structure
  i wrote a custom script to create the file structure. If you need to restart the collection just delete it for now and rerun setup.py

```bash

cd words
python3 setup.py

```
 ---

# Dependency DOT graph generator for Pydgeot
A plugin for [Pydgeot](http://www.github.com/broiledmeat/pydgeot) to generate
[DOT](https://en.wikipedia.org/wiki/DOT_(graph_description_language)) dependency graphs.

### Requirements
- Python 3.*
- [Pydgeot](http://www.github.com/broiledmeat/pydgeot)

### Installation
```bash
git clone https://github.com/broiledmeat/pydgeot_depdot.git pydgeot_depdot
cd pydgeot_depdot
python setup.py install
```

### Configuration
Add `depdot` to your pydgeot.conf `plugins` list. That's it!
```json
{
  "plugins": ["depdot"]
}
```

### Usage
The `depdot` command generates graphs, and stores them in `app/store/deps.dot`. At present, it only takes a
directionality argument, either `forward`, `backward`, or `both` (the default.)

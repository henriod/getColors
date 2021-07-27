# GetMinorColor and GetMajorColor

This is a simple python function exploring the ColorDetect python library to get color with least occurance percentage  or the dominant from a web image 
you just call th function and provide the image url as "https://example.com/image.jpg"

## Installation
Clone the git repo
```bash
git clone https//github.io/henriod/getcolor
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ColorDetect and Requests.

```bash
pip install ColorDetect, requests
```
More about ColorDetect can be found [HERE](https://colordetect.readthedocs.io/en/latest/getting_started.html)

## Usage

```bash
python getcolor.py getMinorColor "image_url"

# returns 'hex'
"#d1234ea"

# returns 'rgb'
"213.0, 45.0 , 20.0"

```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
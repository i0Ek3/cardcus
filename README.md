# cardcus

Customize your bank card face.


## Run

Run command `python3 app.py` and then open `http://127.0.0.1:5000`, after input template name to your console, you can review your card or cut picture for card easily.

## Review

| Home                                                         | Vertical                                                     | Horizon                                                      | Card  Cut Tool                                               |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![](https://github.com/i0Ek3/cardcus/blob/main/images/home.jpg) | ![](https://github.com/i0Ek3/cardcus/blob/main/images/vertical.jpg) | ![](https://github.com/i0Ek3/cardcus/blob/main/images/horizon.jpg) | ![](https://github.com/i0Ek3/cardcus/blob/main/images/cux.jpg) |


## Format

Run command `python3 cardcus.py` to crop the image and format it for the bank card face.

```Shell
$ python3 cardcus.py

Please enter the path to your image: ./images/raw.jpg
Successfully converted image to card format: ./images/output_raw.jpg
```

Specs follows:
- \>= 350 dpi
- 88.5mm \* 55.7mm
- jpg format


## License

MIT

# FV8: A Forced Execution JavaScript Engine for Detecting Evasive Techniques

## Introduction

FV8 (pronounced "favourite") is a specialized version of the V8 engine, enhanced with unique capabilities. FV8 integrates patches from VisibleV8 along with its own custom patches to deliver a powerful tool for code analysis and execution.

### Key Features

- **Forced Execution**: FV8 can force-execute code under specific conditions. This capability is crucial for increasing code coverage, allowing deeper analysis, and uncovering hidden or malicious code that would otherwise remain undetected.
- **Enhanced Code Coverage**: By forcing the execution of more code paths, FV8 enhances the visibility into the code's behavior, making it an invaluable tool for security researchers and developers.

## Usage

### a) Using FV8 Directly

You can use FV8 directly by installing the .deb file of the browser and running it as a normal Chromium browser. The .deb file can be found in `FV8/deb_files`.

Example usage:

```chromium-browser-stable --headless --no-sandbox --disable-gpu --disable-features=NetworkService --js-flags='--no-lazy' https://google.com```

- `--js-flags` is used to pass options directly to V8 instead of passing options to Chromium.
- `--headless` can be removed if you are not executing the browser in a non-visual environment.

### b) Building V8 Yourself

You can build V8 yourself starting from Chromium/V8 and apply our FV8 patches.

The `/patches` directory contains the patches of FV8 that can be applied to the base V8 version.

Example command:

```patch -p1 <$LAST_FV8_PATCH_FILE```

### c) Running the FV8 Crawler to visit websites

To visit topX Tranco URLs:

Install the required packages:

```
pip install -r ./scripts/requirements.txt
export DOCKER_BUILDKIT=0
python ./scripts/vv8-cli.py setup
```

Visit the URLs by running the Python script:

```python crawler_queue_tranco.py```

This script visits websites using the FV8 browser.


## Reference links:

1) [VisibleV8](https://github.com/wspr-ncsu/visiblev8)


## Research Papers

You can read more about the details of our work in the following research papers:

1) **FV8: A Forced Execution JavaScript Engine for Detecting Evasive Techniques** [[PDF]](https://arxiv.org/abs/2405.13175)


If you use *FV8* in your research, consider citing our work using this **Bibtex** entry (link to be updated upon Usenix proceedings):

``` tex
@misc{pantelaios2024fv8,
      title={FV8: A Forced Execution JavaScript Engine for Detecting Evasive Techniques}, 
      author={Nikolaos Pantelaios and Alexandros Kapravelos},
      year={2024},
      eprint={2405.13175},
      archivePrefix={arXiv},
      primaryClass={id='cs.CR' full_name='Cryptography and Security' is_active=True alt_name=None in_archive='cs' is_general=False description='Covers all areas of cryptography and security including authentication, public key cryptosytems, proof-carrying code, etc. Roughly includes material in ACM Subject Classes D.4.6 and E.3.'}
}
```

2) **VisibleV8: In-browser Monitoring of JavaScript in the Wild** [[PDF]](https://kapravelos.com/publications/vv8-imc19.pdf)  
Jordan Jueckstock, Alexandros Kapravelos  
*Proceedings of the ACM Internet Measurement Conference (IMC), 2019*

If you use *VisibleV8* in your research, consider citing our work using this **Bibtex** entry:
``` tex
@conference{vv8-imc19,
  title = {{VisibleV8: In-browser Monitoring of JavaScript in the Wild}},
  author = {Jueckstock, Jordan and Kapravelos, Alexandros},
  booktitle = {{Proceedings of the ACM Internet Measurement Conference (IMC)}},
  year = {2019}
}
```

## License:

TBD, same license as VisibleV8

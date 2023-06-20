# Bifrost

Rainbow bridge for shipping your files to any cloud storage service with the same function calls.

<img src="https://user-images.githubusercontent.com/59074379/226159115-1cfcb221-127f-4574-87ed-b74b4b2c4591.png" width="1000" />

# Table of contents

- [Bifrost](#bifrost)
- [Problem Statement](#problem-statement)
  - [Google Cloud Storage using GCS SDK](#google-cloud-storage-using-gcs-sdk)
  - [Pinata Cloud using Pinata API](#pinata-cloud-using-pinata-api)
  - [Using Bifrost](#using-bifrost)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Changelog](#changelog)
- [Contributors](#contributors)

# Problem Statement

Many projects need to store files in the cloud and different projects might use different cloud storage providers or, sometimes, multiple cloud providers all at once. Using different SDKs with different implementations for each provider can be tedious and time-consuming. Bifrost aims to simplify the process of working with multiple cloud storage providers by providing a consistent API for all of them.

To gain a better understanding of how Bifrost addresses this issue, let's take you on a ride with Thor by comparing two different code samples for working with Google Cloud Storage and Pinata Cloud in a single project: one using a conventional approach and the other using Bifrost.

## Google Cloud Storage using GCS SDK

Without Bifrost, the process of uploading a file to GCS using the Google Cloud Storage client library for Go would typically involve the following steps:

```py
# to be added
```

## Pinata Cloud using Pinata API

...and for Pinata Cloud, the usual way of uploading a file in Go would be something along the following steps:

```py
# to be added
```

We can already see the challenges of the conventional methods since they require you to learn to use multiple packages with separate implementation patterns. Now this is why `Bifrost` comes in! With Bifrost, you can mount rainbow bridges to the providers you want and use the same set of functions to upload files through any of these mounted bridges. This makes it much easier to work with multiple providers and streamlines the development process to just one learning curve.

Now, let's see how we can revamp the two samples above into something much more exciting with Bifrost.

## Using Bifrost

```py
# to be added
```

The above example clearly demonstrates the speed, simplicity, and ease of use that Bifrost offers. Now you know what it feels like to ride with Thor!

# Installation

```bash
pip install byfrost
```

# Usage

If you want to learn more about how Bifrost is creating different methods to make it easier to use different cloud providers, you can follow these links:

- [Google Cloud Storage (GCS)](gcs\doc.md)
- [Amazon S3](s3\doc.md)
- [Pinata Cloud](pinata\doc.md)

# Variants

Bifrost also exists in other forms and languages and you are free to start a new variant of bifrost in any other form or language of your choice. For now, below are the know variants of bifrost.

- [x] [Bifrost in Golang](https://github.com/opensaucerer/bifrost)
- [x] [Bifrost CLI](https://github.com/showbaba/bifrost-cli)

# Contributing

Bifrost is an open source project and we welcome contributions of all kinds. Please read our [contributing guide](./contributing.md) to learn about our development process, how to propose bugfixes and improvements, and how to build and test your changes to Bifrost.

# License

Bifrost is [MIT licensed](./LICENSE).

# Changelog

See [changelog](./changelog.md) for more details.

# Contributors

<a href="https://github.com/ifihan/byfrost/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ifihan/byfrost" />
</a>

Made with [contrib.rocks](https://contrib.rocks).

# Google API Client Checker

A Python script to verify the validity of Google API client credentials.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Description

This script verifies the validity of Google API client credentials (Client ID and Client Secret) by making a request to the Google OAuth2 token info endpoint.

## Installation

1. Make sure you have Python installed on your system.
2. Install the requests and colorama libraries using pip:

    ```bash
    pip install requests colorama
    ```

## Usage

1. Run the script `google_checker.py` with your Google API client ID and client secret as command-line arguments:

    ```bash
    python google_checker.py client_id client_secret
    ```

Replace `client_id` and `client_secret` with your actual Google API client ID and client secret.

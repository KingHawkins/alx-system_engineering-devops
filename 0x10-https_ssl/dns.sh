#!/bin/bash

# Define the subdomains to query
SUBDOMAINS=("www" "lb-01" "web-01" "web-02")

# Loop through each subdomain and query its DNS record
for SUBDOMAIN in "${SUBDOMAINS[@]}"
do
  echo "DNS record for $SUBDOMAIN:"
  dig +short $SUBDOMAIN.bobhawkins.tech
done

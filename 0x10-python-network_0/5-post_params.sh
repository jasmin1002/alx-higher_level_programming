#!/bin/bash
# Script uses curl to perform post method
curl -sX POST -d email='test%40gmail%2Ecom' subject='I+will+always+be+here+for+PLD' $1

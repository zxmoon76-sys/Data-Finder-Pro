#!/bin/bash
echo "Installing Data Finder Pro..."
chmod +x finder.py
# সঠিক পদ্ধতিতে কপি করা যাতে পাইথন হিসেবে রান হয়
cp finder.py $PREFIX/bin/data-finder
echo "Installation Complete! Now you can type 'data-finder' from anywhere."

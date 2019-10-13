#!/bin/bash
ping -c 1 ya.ru >/dev/null 2>&1 && echo "There is connction" || echo "no connction"

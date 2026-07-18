# Copyright 2024 The IREE Authors
#
# Licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

from sys import exit

from .main import iree_build_main


def main(
    args: list[str] | None = None,
):
    iree_build_main(args=args)


if __name__ == "__main__":
    exit(main())

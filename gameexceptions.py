#!/usr/bin/env python2


class HorizontalBorderHitError(Exception):
    def __init__(self):
        Exception.__init__(self)


class VerticalBorderHitError(Exception):
    def __init__(self):
        Exception.__init__(self)


class PlayerHitError(Exception):
    def __init__(self):
        Exception.__init__(self)

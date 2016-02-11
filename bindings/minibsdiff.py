# libminibsdiff python wrapper
#
# Copyright(c) 2016 Intel Corporation.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import ctypes

minibsdiff = ctypes.CDLL('libminibsdiff.so')

class MBSDIFF:

    def __init__(self):
        self.version = 1

    def bsdiff(self, c_old_buffer, c_new_buffer):
        c_patch_buffer = ctypes.create_string_buffer(minibsdiff.bsdiff_patchsize_max(len(c_old_buffer), len(c_new_buffer)))
        status = minibsdiff.bsdiff(c_old_buffer, len(c_old_buffer), c_new_buffer, len(c_new_buffer), c_patch_buffer, len(c_patch_buffer))
        assert (status > 0)
        return ctypes.string_at(c_patch_buffer, status)

    def bspatch(self, c_old_buffer, c_patch_buffer):
        c_new_buffer = ctypes.create_string_buffer(minibsdiff.bspatch_newsize(len(c_patch_buffer), len(c_patch_buffer)))
        status = minibsdiff.bspatch(c_old_buffer, len(c_old_buffer), c_patch_buffer, len(c_patch_buffer), c_new_buffer, len(c_new_buffer))
        assert (status == 0)
        return ctypes.string_at(c_new_buffer, len(c_new_buffer))

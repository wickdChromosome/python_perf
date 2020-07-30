cdef extern from "sumarrayheader.h"
  cdef int arraysum(int[])

#Python entry point - calling C function
def sumarray(inarray)
  return sum_array(inarray)
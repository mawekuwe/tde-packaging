#include "kdemacros.h"
extern "C" KDE_EXPORT void *init_libkopete_msn_shared();
extern "C" KDE_EXPORT void *init_kopete_msn() { return init_libkopete_msn_shared(); }

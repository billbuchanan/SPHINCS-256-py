import os
from WOTSplus import WOTSplus
from SPHINCS import SPHINCS


def test_WOTSplus():
    n = 256
    m = os.urandom(n // 8)
    seed = os.urandom(n // 8)
    w = 16
    masks = [os.urandom(n // 8) for _ in range(w - 1)]
    wots = WOTSplus(n=n, w=w, F=SPHINCS().F, Gl=SPHINCS().Glambda)
    pk = wots.keygen(seed, masks)
    sig = wots.sign(m, seed, masks)
    assert pk == wots.verify(m, sig, masks)


def test_WOTSplus_ref():
    """This test-case is derived from the SPHINCS reference implementation"""
    n = 256
    m = bytes(range(32))
    seed = bytes(range(32, 64))
    w = 16
    masks = [bytes(range(i, 32+i)) for i in range(w - 1)]
    wots = WOTSplus(n=n, w=w, F=SPHINCS().F, Gl=SPHINCS().Glambda)
    pk = wots.keygen(seed, masks)
    sig = wots.sign(m, seed, masks)
    assert pk == wots.verify(m, sig, masks)
    assert sig == [bytes([0x11, 0xD8, 0x5B, 0x22, 0xA5, 0xAB, 0x55, 0x9B,
                          0x5D, 0x10, 0x6F, 0xDC, 0x08, 0x25, 0xDE, 0x67,
                          0x7C, 0x28, 0x74, 0x0B, 0x05, 0x68, 0x98, 0x99,
                          0x4E, 0x14, 0x1A, 0xF4, 0xBF, 0x04, 0x6E, 0x73]),
                   bytes([0xAD, 0x43, 0x24, 0x33, 0x86, 0x8F, 0xB9, 0x9F,
                          0x09, 0xCD, 0xDF, 0x03, 0xE7, 0x0D, 0x5E, 0xDE,
                          0xDE, 0xCE, 0x9F, 0x8E, 0xE9, 0x17, 0x39, 0xBF,
                          0xF3, 0x12, 0x7E, 0x1D, 0x66, 0x82, 0x80, 0x8F]),
                   bytes([0xAC, 0x3F, 0x87, 0xCB, 0xAA, 0x4A, 0x31, 0x1D,
                          0xE1, 0xA5, 0x9C, 0x1D, 0xBA, 0x2C, 0x05, 0x7E,
                          0xCF, 0x13, 0xEE, 0x87, 0x35, 0xBB, 0xDD, 0xA6,
                          0xD3, 0x43, 0xD3, 0xCE, 0xC2, 0xB7, 0x3E, 0xE7]),
                   bytes([0xA6, 0x85, 0x62, 0x12, 0x3F, 0xF2, 0xB2, 0x49,
                          0xF0, 0x21, 0x0A, 0x47, 0xCD, 0xE3, 0x6A, 0x89,
                          0x32, 0x08, 0x26, 0x91, 0x28, 0x37, 0x14, 0x65,
                          0xED, 0x29, 0xF0, 0x54, 0x55, 0x07, 0xE1, 0xB7]),
                   bytes([0x26, 0x05, 0x52, 0x3F, 0x3B, 0x54, 0xD7, 0x02,
                          0x2E, 0xFE, 0x6A, 0xC8, 0xD3, 0xEA, 0xA2, 0xAF,
                          0xD8, 0xDD, 0x02, 0x7A, 0xD9, 0xA3, 0x4B, 0x90,
                          0x93, 0x26, 0x6F, 0x78, 0x83, 0x98, 0x81, 0xD1]),
                   bytes([0xAD, 0x46, 0xF2, 0xBD, 0x8F, 0xE9, 0xCB, 0xA4,
                          0x5E, 0x1C, 0x06, 0xB6, 0x35, 0x26, 0x89, 0x4E,
                          0x1D, 0x79, 0x90, 0xE3, 0x94, 0xDB, 0x34, 0xB5,
                          0x0C, 0x4C, 0xBA, 0xA7, 0x59, 0xE6, 0x39, 0x9D]),
                   bytes([0x89, 0x18, 0xD4, 0xC5, 0x72, 0xB9, 0xB0, 0xDD,
                          0xFE, 0x63, 0xAD, 0xD3, 0xCC, 0xB0, 0xFC, 0xD9,
                          0x21, 0x13, 0x96, 0x0C, 0x1B, 0x0F, 0xDA, 0xD3,
                          0xC7, 0x06, 0x71, 0x4C, 0x8E, 0xB3, 0x1F, 0x20]),
                   bytes([0xB2, 0xBF, 0x3A, 0x65, 0x25, 0xF0, 0x2F, 0xE5,
                          0x98, 0x53, 0xC9, 0xED, 0x4D, 0xAE, 0x02, 0x7B,
                          0x1B, 0x20, 0x81, 0x15, 0x79, 0xEE, 0x6D, 0x1C,
                          0x2C, 0xF4, 0xDE, 0x23, 0xE7, 0x0D, 0x9B, 0x09]),
                   bytes([0xDD, 0xC5, 0x9B, 0x98, 0x54, 0x74, 0xC0, 0x7C,
                          0xF1, 0x42, 0xEF, 0x97, 0x45, 0x00, 0x57, 0x89,
                          0xDF, 0x62, 0x04, 0x2A, 0xB7, 0x05, 0xD8, 0x2B,
                          0x9B, 0x32, 0x9E, 0x13, 0xAB, 0x3F, 0x60, 0x7C]),
                   bytes([0xD7, 0x62, 0xD7, 0x42, 0x92, 0x13, 0x15, 0x2F,
                          0xC7, 0x2E, 0xC4, 0x16, 0x4C, 0x4A, 0x20, 0x30,
                          0x50, 0xF7, 0x81, 0x2A, 0x60, 0x9E, 0x50, 0xFF,
                          0xDE, 0x0E, 0x9F, 0x57, 0xB3, 0xBB, 0xC6, 0xE2]),
                   bytes([0x79, 0x61, 0xA7, 0xD7, 0x22, 0x00, 0x40, 0x3A,
                          0x3B, 0x4C, 0x70, 0x33, 0x15, 0x2D, 0xB0, 0x09,
                          0x9C, 0x46, 0xEF, 0xEF, 0xEB, 0xA9, 0x42, 0x9D,
                          0xCC, 0xA8, 0x0E, 0x13, 0xD4, 0xC5, 0x06, 0x5F]),
                   bytes([0x44, 0xAB, 0xEF, 0x27, 0x43, 0xCE, 0xC1, 0xDC,
                          0xF2, 0x0A, 0xDE, 0x53, 0x82, 0x12, 0xE7, 0x37,
                          0xBA, 0x0A, 0xC7, 0xCF, 0xAC, 0x2B, 0x39, 0x08,
                          0xC2, 0x92, 0x76, 0xDB, 0x08, 0x8D, 0x4A, 0x4F]),
                   bytes([0x0C, 0x3D, 0x04, 0x7B, 0x76, 0xE3, 0x30, 0xA5,
                          0x71, 0x49, 0x56, 0xB3, 0xB6, 0xF9, 0x9F, 0x9E,
                          0xE1, 0xC1, 0x84, 0xB5, 0xB5, 0xB3, 0xF9, 0xFC,
                          0xBC, 0x4D, 0xC8, 0x78, 0xA5, 0x99, 0x20, 0x54]),
                   bytes([0x76, 0x89, 0x21, 0xFC, 0x2B, 0x08, 0xF6, 0x50,
                          0x7D, 0x44, 0x29, 0x40, 0xF1, 0xDA, 0x5A, 0x3F,
                          0xEC, 0x11, 0xAE, 0x00, 0x07, 0x7A, 0x6C, 0x73,
                          0xF2, 0xD8, 0x92, 0x09, 0x7F, 0xF5, 0x95, 0x94]),
                   bytes([0xD4, 0x53, 0x75, 0x89, 0xCF, 0xF3, 0x5D, 0x10,
                          0xD9, 0x8F, 0x5D, 0x9A, 0x39, 0xEB, 0x44, 0x6C,
                          0x21, 0x46, 0xA7, 0xF6, 0x54, 0xC3, 0xE7, 0xDE,
                          0x6A, 0x1D, 0x9F, 0x6D, 0xA5, 0x24, 0xA0, 0xB5]),
                   bytes([0xA8, 0x47, 0x1B, 0x7C, 0xF9, 0x70, 0x8E, 0x8E,
                          0x57, 0x10, 0x93, 0x33, 0xF0, 0x50, 0x60, 0xCF,
                          0x3D, 0xE9, 0x3C, 0xCF, 0x5B, 0x42, 0x39, 0x75,
                          0x64, 0xD1, 0xA5, 0x09, 0x8C, 0xBA, 0xD2, 0x5E]),
                   bytes([0x07, 0x11, 0xA9, 0x75, 0x19, 0xEA, 0x9C, 0x02,
                          0xC4, 0xFC, 0xBF, 0x12, 0xD2, 0x74, 0xF6, 0x22,
                          0xF6, 0x56, 0xE5, 0x9B, 0x86, 0x66, 0xE2, 0x20,
                          0xDE, 0xCD, 0xE8, 0x4E, 0x20, 0xC1, 0x04, 0x50]),
                   bytes([0x99, 0x52, 0xFD, 0x64, 0x4E, 0x01, 0xC7, 0xB4,
                          0x76, 0xF6, 0xBC, 0xD3, 0x81, 0xDA, 0xA1, 0x82,
                          0x7D, 0xEE, 0x01, 0x98, 0x80, 0x98, 0xED, 0x3E,
                          0xC8, 0xB2, 0xC3, 0x39, 0xF6, 0x1A, 0xF1, 0xA6]),
                   bytes([0x5B, 0x43, 0x17, 0x14, 0x35, 0xCD, 0x8F, 0x4D,
                          0xF0, 0x5C, 0x3D, 0x57, 0xD0, 0x41, 0x6C, 0xB2,
                          0x61, 0xB6, 0x17, 0xF2, 0xE9, 0xE6, 0x46, 0x4E,
                          0x92, 0xCD, 0x49, 0x96, 0x3D, 0x55, 0x1D, 0xFE]),
                   bytes([0xFA, 0x17, 0xE0, 0x74, 0xD1, 0x70, 0x61, 0x52,
                          0xB9, 0x7C, 0xB8, 0x23, 0x4B, 0x67, 0x69, 0xBA,
                          0x7B, 0x8F, 0xCA, 0x69, 0x2A, 0x8E, 0x8B, 0x4F,
                          0x99, 0xEF, 0x51, 0x5A, 0x90, 0x48, 0x3A, 0x9A]),
                   bytes([0x3D, 0x6B, 0x23, 0x8F, 0xE0, 0xEE, 0xB5, 0x1C,
                          0x5D, 0x38, 0x14, 0x98, 0x09, 0xF3, 0x1B, 0xBF,
                          0xFE, 0x17, 0xC8, 0xB1, 0x8E, 0x20, 0xC5, 0x5D,
                          0xF4, 0xB1, 0x19, 0x36, 0x18, 0x2C, 0xE0, 0xBE]),
                   bytes([0x7C, 0x74, 0xD6, 0x2A, 0x3D, 0x8D, 0xF3, 0x35,
                          0x5A, 0xFD, 0xBB, 0x95, 0x4F, 0xF2, 0x7A, 0xAA,
                          0x5D, 0xCE, 0x50, 0x2B, 0x52, 0xBE, 0xF6, 0x98,
                          0x71, 0x8A, 0x16, 0xEB, 0xD6, 0xAD, 0x03, 0x0D]),
                   bytes([0xE3, 0x64, 0x01, 0x35, 0xB6, 0x81, 0x9E, 0xB2,
                          0xE0, 0x41, 0x0A, 0xBA, 0xCD, 0x14, 0x29, 0xED,
                          0xB8, 0x94, 0x3C, 0x6D, 0x2D, 0x63, 0x21, 0x16,
                          0x18, 0x9A, 0x2F, 0x50, 0x7B, 0x0D, 0xE8, 0x9F]),
                   bytes([0x70, 0xD6, 0x41, 0x70, 0xAF, 0x00, 0x83, 0x0A,
                          0x46, 0x9E, 0xCD, 0x86, 0xA4, 0xE2, 0xBE, 0xEA,
                          0xCD, 0x9F, 0xB9, 0x91, 0x14, 0x89, 0xED, 0x4E,
                          0x63, 0x60, 0x7E, 0x09, 0xEA, 0xB3, 0x73, 0x8D]),
                   bytes([0xDF, 0x04, 0x52, 0x09, 0x59, 0xD6, 0x26, 0xAE,
                          0x6E, 0xDD, 0xCF, 0x32, 0xDF, 0x8E, 0x08, 0x28,
                          0xA4, 0x45, 0x19, 0x3C, 0xFE, 0xAF, 0x1F, 0xA8,
                          0x9B, 0x99, 0x3C, 0xD3, 0x9F, 0x01, 0x02, 0x9A]),
                   bytes([0x47, 0x3C, 0x4A, 0xE6, 0x41, 0x0B, 0xFB, 0x91,
                          0xAE, 0xF5, 0xA9, 0xA1, 0x19, 0x01, 0xB1, 0x2D,
                          0xBB, 0xDA, 0xB7, 0x09, 0x33, 0xE6, 0x0D, 0x00,
                          0xD1, 0xA1, 0x79, 0xC3, 0xA3, 0xFB, 0x26, 0x05]),
                   bytes([0x31, 0x7F, 0x64, 0x5A, 0x5B, 0x2D, 0xA6, 0x9D,
                          0x76, 0xF9, 0x84, 0x53, 0x3E, 0x77, 0x0A, 0xB8,
                          0x91, 0x98, 0x64, 0x8A, 0x15, 0x2A, 0xF6, 0xDA,
                          0x23, 0xD0, 0x2E, 0xAF, 0x37, 0x3C, 0xDB, 0xE9]),
                   bytes([0x60, 0x09, 0xB4, 0x02, 0x5B, 0x3A, 0x3D, 0xB9,
                          0xE8, 0x8D, 0x40, 0x62, 0x5A, 0x48, 0xFC, 0x00,
                          0x64, 0x1B, 0x1B, 0x4E, 0x31, 0x1D, 0xFD, 0x90,
                          0x43, 0xAA, 0x69, 0x9A, 0xBE, 0x18, 0x3F, 0x76]),
                   bytes([0xB3, 0x4D, 0xED, 0xFF, 0x07, 0x77, 0xE5, 0xAD,
                          0xB5, 0x26, 0xC2, 0xF9, 0x2C, 0x57, 0x69, 0x7C,
                          0x5C, 0xBC, 0x59, 0x07, 0x18, 0x1A, 0x5F, 0xF3,
                          0x05, 0xD9, 0x70, 0x0B, 0x87, 0x65, 0xFF, 0x7D]),
                   bytes([0x7C, 0x1B, 0xC6, 0x30, 0xF6, 0x45, 0x9D, 0x88,
                          0x69, 0xF3, 0x4C, 0xC0, 0x3A, 0xD7, 0xC9, 0xA8,
                          0x7D, 0x41, 0xA8, 0x9D, 0x13, 0x50, 0x21, 0xF4,
                          0xC4, 0x02, 0xD8, 0xB7, 0x29, 0xB2, 0x8C, 0x5C]),
                   bytes([0xC3, 0x5F, 0xE3, 0xE7, 0xC2, 0x33, 0x6E, 0x36,
                          0x72, 0x85, 0xA2, 0x3B, 0x6E, 0x1D, 0x96, 0x7A,
                          0xD6, 0x8A, 0xA7, 0x24, 0x72, 0xAA, 0x1A, 0xB7,
                          0x61, 0x90, 0x54, 0x6B, 0x0F, 0xAA, 0x64, 0x24]),
                   bytes([0xA0, 0xCF, 0x1F, 0xBD, 0x0B, 0x9B, 0xE7, 0xE5,
                          0x3E, 0xE7, 0xB4, 0x6E, 0x54, 0xDA, 0x5F, 0x4D,
                          0xA2, 0x78, 0xAE, 0x50, 0xA2, 0x6A, 0x22, 0x60,
                          0x34, 0x9C, 0x77, 0xF2, 0xEF, 0x26, 0xF9, 0x14]),
                   bytes([0x5C, 0x42, 0x0B, 0x50, 0x21, 0xAF, 0x47, 0x02,
                          0x49, 0x51, 0x4B, 0xD9, 0x38, 0x74, 0x53, 0x5E,
                          0xD3, 0xEB, 0xC5, 0x89, 0x52, 0xCF, 0xA7, 0xD8,
                          0x9B, 0x34, 0x58, 0x62, 0x37, 0x56, 0x31, 0x75]),
                   bytes([0x57, 0xBB, 0x89, 0x88, 0xC8, 0x52, 0xEA, 0xB4,
                          0xF4, 0xF6, 0x4C, 0xAF, 0x87, 0xFF, 0xA2, 0xA4,
                          0x80, 0x4E, 0x12, 0xE1, 0x2B, 0xE6, 0xCB, 0xE5,
                          0x65, 0xC5, 0xC7, 0x46, 0x9E, 0x0B, 0xE3, 0x28]),
                   bytes([0x02, 0x38, 0x6B, 0xCB, 0x64, 0xDA, 0x26, 0xEB,
                          0x69, 0xB6, 0x7B, 0xC8, 0xCF, 0xA9, 0xDE, 0xC5,
                          0x66, 0x02, 0x98, 0xAF, 0x68, 0xD6, 0x5E, 0x99,
                          0xB8, 0xC9, 0xC3, 0xC3, 0x4E, 0x62, 0x9D, 0x26]),
                   bytes([0x46, 0x5C, 0xCC, 0x08, 0x70, 0x49, 0xCD, 0x00,
                          0x12, 0x59, 0xF7, 0x14, 0x12, 0x53, 0x03, 0xA4,
                          0x40, 0xD7, 0x3D, 0x0E, 0xC2, 0x79, 0xF1, 0x90,
                          0xFB, 0x3B, 0x88, 0x07, 0x13, 0xC9, 0x8A, 0x3C]),
                   bytes([0x6E, 0xA7, 0x31, 0x5E, 0x36, 0xBB, 0x31, 0xBC,
                          0x51, 0x1D, 0xBF, 0x01, 0x96, 0x65, 0x90, 0xA9,
                          0x96, 0xF1, 0x1C, 0x2A, 0xE6, 0xEB, 0xAA, 0x97,
                          0xC7, 0x61, 0x68, 0xE0, 0x52, 0x82, 0xA3, 0xC5]),
                   bytes([0x63, 0x09, 0x85, 0xCC, 0x33, 0x86, 0x11, 0xA2,
                          0xB4, 0xD3, 0xF0, 0x58, 0xFC, 0x92, 0xDF, 0xB4,
                          0x63, 0xBE, 0x67, 0x20, 0x2D, 0x3D, 0xA7, 0x9A,
                          0xFA, 0x36, 0xAA, 0x4B, 0xD4, 0x17, 0x8D, 0x07]),
                   bytes([0xC1, 0x15, 0xEB, 0x3B, 0xD0, 0xAF, 0xE3, 0xEA,
                          0xB0, 0x84, 0x68, 0xCF, 0xC5, 0x90, 0xCF, 0x27,
                          0x0C, 0x17, 0x38, 0xAC, 0x80, 0x0A, 0x11, 0xBD,
                          0x77, 0xB9, 0x7F, 0x95, 0xF1, 0xC6, 0x72, 0xC6]),
                   bytes([0x77, 0x95, 0xF9, 0x30, 0x58, 0x10, 0x33, 0xC1,
                          0x7B, 0x65, 0xFF, 0xB5, 0x76, 0xAB, 0x41, 0xE6,
                          0xE1, 0x2A, 0xE9, 0xEF, 0xAF, 0x93, 0xE3, 0xD9,
                          0x83, 0x3F, 0x7E, 0xF1, 0x1A, 0x1A, 0x2E, 0xB2]),
                   bytes([0x04, 0xBF, 0x7D, 0x84, 0x2C, 0xCD, 0x7A, 0x43,
                          0x64, 0x7C, 0xB6, 0x8C, 0xB7, 0x03, 0xDB, 0x81,
                          0xAE, 0x04, 0xE5, 0xEE, 0x2F, 0x6B, 0x13, 0x74,
                          0x00, 0x2C, 0x8E, 0xE7, 0x97, 0x17, 0x3A, 0x12]),
                   bytes([0xDC, 0xF2, 0xA1, 0xAA, 0xA9, 0xE1, 0x14, 0xF9,
                          0x3A, 0x55, 0xE1, 0xF2, 0x75, 0xB9, 0xC2, 0x37,
                          0xA9, 0x6C, 0x36, 0x2D, 0x47, 0xBC, 0xFF, 0x22,
                          0x2C, 0xFC, 0xDF, 0x83, 0x73, 0x09, 0x5D, 0x8A]),
                   bytes([0x55, 0x5C, 0xDA, 0x71, 0x22, 0x0B, 0x66, 0x54,
                          0xF9, 0x95, 0x73, 0xC4, 0xF4, 0x75, 0xC7, 0x9E,
                          0x43, 0xFB, 0x41, 0xFD, 0xC2, 0x25, 0xB5, 0xA7,
                          0xD4, 0x07, 0xAC, 0xBF, 0xBF, 0x88, 0xBB, 0x79]),
                   bytes([0xCE, 0x7E, 0x1C, 0xA5, 0x43, 0x9C, 0xFF, 0x25,
                          0x65, 0xC2, 0x31, 0x22, 0x40, 0x07, 0xCF, 0x00,
                          0xA3, 0x6B, 0x86, 0x6F, 0xB8, 0x48, 0x8B, 0x11,
                          0xA5, 0xAC, 0x19, 0x69, 0x8C, 0x8D, 0x66, 0xC5]),
                   bytes([0xA2, 0xDF, 0x74, 0x94, 0xA6, 0x1E, 0x73, 0x14,
                          0xB1, 0xD3, 0x4F, 0xDD, 0x1A, 0xF8, 0xF1, 0x4F,
                          0x01, 0x66, 0x1A, 0x63, 0xF7, 0x15, 0xDD, 0x05,
                          0x6C, 0xD6, 0xE8, 0xC8, 0xBD, 0xDD, 0xB7, 0x30]),
                   bytes([0x6F, 0x1B, 0xDD, 0xF8, 0xF0, 0x87, 0x2E, 0xE8,
                          0x25, 0x1D, 0x7A, 0x7E, 0x95, 0x6D, 0xA8, 0x9A,
                          0x26, 0x4F, 0xCE, 0x8D, 0x0D, 0x38, 0xFB, 0x11,
                          0x96, 0x90, 0x56, 0x7E, 0x6F, 0x47, 0x43, 0x80]),
                   bytes([0x71, 0xCD, 0x2A, 0xDB, 0x3A, 0x0A, 0x29, 0xD1,
                          0xC2, 0xD9, 0x33, 0x64, 0xDC, 0x6D, 0x82, 0x5A,
                          0x8F, 0x69, 0x99, 0x88, 0xBF, 0x9E, 0xBA, 0xC5,
                          0x97, 0x13, 0xA4, 0xD1, 0x3D, 0xCB, 0x85, 0x34]),
                   bytes([0xAC, 0xAA, 0x9F, 0x1D, 0xD7, 0xE4, 0xC0, 0x59,
                          0xC7, 0xD6, 0xC4, 0xAE, 0xB7, 0x1F, 0x87, 0x52,
                          0xDB, 0x7E, 0xB2, 0xED, 0x93, 0xB2, 0x11, 0x73,
                          0x3B, 0x94, 0x45, 0xCB, 0xF2, 0xE3, 0xD8, 0xF7]),
                   bytes([0xFA, 0x3F, 0x55, 0x92, 0x6F, 0xDA, 0x24, 0x2A,
                          0xE5, 0x20, 0x00, 0x63, 0xCA, 0xAC, 0x73, 0x66,
                          0x65, 0x81, 0xE5, 0x9D, 0x2C, 0xEB, 0xF5, 0xBB,
                          0xA9, 0x2E, 0x8B, 0xA4, 0x55, 0x4F, 0xE4, 0x70]),
                   bytes([0x45, 0xE9, 0xA6, 0x9E, 0x95, 0x1A, 0x21, 0x31,
                          0xF2, 0xE0, 0x27, 0xE1, 0xC7, 0xE8, 0xC9, 0xE2,
                          0xFE, 0x05, 0x7C, 0x7A, 0x10, 0x82, 0x29, 0xA5,
                          0x22, 0x5E, 0xD0, 0x21, 0xCA, 0x89, 0xC6, 0xEB]),
                   bytes([0xAD, 0x62, 0xAB, 0x67, 0x46, 0x05, 0x20, 0x7E,
                          0x82, 0xFF, 0x9D, 0xD9, 0x6F, 0x47, 0xF2, 0x53,
                          0x46, 0x9D, 0x08, 0x44, 0xB4, 0x73, 0x35, 0x5A,
                          0x2A, 0xF4, 0x54, 0xCD, 0xAE, 0x6A, 0xA2, 0x97]),
                   bytes([0xD1, 0x1D, 0x65, 0xF6, 0x64, 0x68, 0x3E, 0x3E,
                          0xC5, 0x10, 0x9D, 0x24, 0x06, 0xD4, 0xCC, 0x8F,
                          0x63, 0x06, 0xF4, 0xD7, 0x22, 0x0C, 0x44, 0xEB,
                          0xDE, 0x0E, 0x6C, 0xDA, 0xA5, 0x04, 0xDE, 0x13]),
                   bytes([0x63, 0x2F, 0x27, 0x19, 0xBE, 0x41, 0x2B, 0xA6,
                          0xA8, 0x60, 0xDF, 0x7D, 0x08, 0xE6, 0x6B, 0x82,
                          0xC3, 0xD0, 0xE3, 0x30, 0x3D, 0xEF, 0x0E, 0x43,
                          0x1F, 0x64, 0xDF, 0xB7, 0xBA, 0xA7, 0x0A, 0x3D]),
                   bytes([0x66, 0x05, 0xE1, 0x74, 0xF1, 0xD3, 0x70, 0xDC,
                          0x4B, 0x11, 0x51, 0x3F, 0x59, 0xB3, 0x79, 0x94,
                          0xF6, 0x2F, 0x24, 0x6A, 0xEC, 0x2E, 0xB0, 0xAB,
                          0xE3, 0x29, 0xED, 0xAD, 0xC6, 0x1F, 0x8C, 0x71]),
                   bytes([0xAF, 0xC4, 0xBA, 0x01, 0x88, 0x88, 0x38, 0x55,
                          0x49, 0x6B, 0x5F, 0xBC, 0xA4, 0xF6, 0x53, 0x3A,
                          0xDB, 0x35, 0x37, 0xD9, 0xC5, 0x15, 0xC9, 0x56,
                          0xC8, 0x43, 0x70, 0x9B, 0xAD, 0x11, 0x6F, 0x97]),
                   bytes([0xBE, 0x52, 0x0E, 0x4C, 0xA2, 0x48, 0x0D, 0x47,
                          0xB2, 0xBD, 0x47, 0x59, 0xCE, 0x62, 0xAD, 0x2D,
                          0xC5, 0xF4, 0xF6, 0xB3, 0x2D, 0x0C, 0xAE, 0xB5,
                          0x95, 0x47, 0x93, 0xB3, 0x57, 0x01, 0xEE, 0x8E]),
                   bytes([0xC6, 0xB4, 0x4D, 0xC6, 0x4C, 0xC8, 0x74, 0xD0,
                          0x7F, 0x7D, 0x95, 0x51, 0x7B, 0xAD, 0x89, 0x4B,
                          0x83, 0x11, 0xFF, 0xCD, 0x1F, 0x65, 0x82, 0xC2,
                          0xFC, 0x80, 0xEB, 0xD5, 0x10, 0x7A, 0x8E, 0xA9]),
                   bytes([0xF2, 0xB3, 0x0D, 0x8A, 0xE0, 0xE5, 0x05, 0x6F,
                          0xA2, 0xF2, 0x98, 0xF8, 0xCE, 0xC3, 0x8A, 0x17,
                          0xB6, 0x74, 0x5F, 0x16, 0x29, 0x73, 0x56, 0x9F,
                          0x91, 0xE3, 0xDA, 0x75, 0x82, 0x61, 0x0E, 0x54]),
                   bytes([0x05, 0x97, 0x92, 0x5B, 0x1D, 0xFF, 0x2F, 0x9F,
                          0xC7, 0x29, 0x3D, 0xA6, 0xAB, 0xC4, 0x86, 0x3D,
                          0xD3, 0x16, 0x18, 0xE6, 0x28, 0x18, 0xDD, 0x9C,
                          0xCE, 0xE9, 0x38, 0x4F, 0xF6, 0xD1, 0xE7, 0x0E]),
                   bytes([0xAA, 0x60, 0x49, 0xEA, 0x2E, 0x27, 0xF8, 0xBE,
                          0xDE, 0x47, 0xF5, 0x7B, 0x0D, 0x36, 0x9F, 0xCB,
                          0xD1, 0xC7, 0xE7, 0xAB, 0x84, 0xED, 0x48, 0x37,
                          0x2F, 0x79, 0x2B, 0xE6, 0x85, 0x38, 0x62, 0x78]),
                   bytes([0xDA, 0x43, 0x5B, 0x2E, 0x83, 0x65, 0x26, 0x67,
                          0xE4, 0xD8, 0x25, 0x8F, 0x14, 0x7B, 0x70, 0x41,
                          0x0C, 0x51, 0x71, 0xE1, 0x4A, 0x2C, 0x93, 0x72,
                          0xBA, 0x3F, 0xDE, 0x6F, 0x53, 0x98, 0x71, 0x10]),
                   bytes([0xAE, 0x1F, 0x5B, 0x2C, 0xDA, 0x9F, 0xFD, 0x93,
                          0x24, 0x9E, 0x83, 0x1A, 0x8D, 0x62, 0x75, 0xAB,
                          0x03, 0xC0, 0xE6, 0xB9, 0xF1, 0xC0, 0x3C, 0x08,
                          0xCB, 0x1E, 0xC2, 0x35, 0x6E, 0x3C, 0xC7, 0x0D]),
                   bytes([0x5D, 0xEE, 0x4B, 0xC7, 0x3D, 0xBD, 0xA8, 0xCA,
                          0x56, 0xDB, 0x9A, 0x37, 0xC8, 0x3A, 0xCB, 0x60,
                          0x2D, 0x45, 0xD7, 0x7B, 0x1E, 0x97, 0x8E, 0x85,
                          0x16, 0x36, 0x9A, 0x96, 0x61, 0x73, 0x07, 0xEF]),
                   bytes([0x4B, 0x67, 0xD3, 0xCF, 0xD2, 0xEF, 0xEC, 0x9E,
                          0x64, 0x1E, 0x5D, 0x85, 0x3C, 0x13, 0x23, 0x34,
                          0xA7, 0x80, 0x9B, 0xC4, 0x2C, 0x3C, 0xB9, 0xF2,
                          0xF7, 0x38, 0x93, 0xDF, 0x3D, 0xFE, 0x65, 0x44]),
                   bytes([0x82, 0x0F, 0xD1, 0xD7, 0x25, 0x4A, 0xC1, 0x78,
                          0x69, 0x74, 0xA0, 0xB5, 0x3A, 0xAD, 0x51, 0xF3,
                          0x58, 0x78, 0xBD, 0x5E, 0x18, 0x9B, 0xA7, 0xB4,
                          0x82, 0x1A, 0x28, 0xD9, 0x1B, 0xB1, 0x18, 0xBD]),
                   bytes([0xC4, 0xCE, 0xFC, 0x80, 0x5F, 0x10, 0x83, 0xA9,
                          0xE7, 0x9D, 0xB9, 0x03, 0x48, 0x1A, 0x90, 0x44,
                          0xDB, 0xB7, 0x06, 0x39, 0xD0, 0x6B, 0x96, 0xFE,
                          0x80, 0x71, 0x16, 0x74, 0x31, 0x79, 0x55, 0x35]),
                   bytes([0xAD, 0x22, 0xB8, 0xB8, 0xC7, 0x2C, 0x5B, 0x9F,
                          0x1D, 0x24, 0x9A, 0xD4, 0x1D, 0x48, 0x90, 0x5F,
                          0x4F, 0x70, 0x57, 0x1D, 0xF2, 0x2F, 0x8D, 0xAF,
                          0xBB, 0x0A, 0xC8, 0x14, 0x09, 0xA8, 0xB0, 0xC5])]

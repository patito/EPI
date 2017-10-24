package main

import "testing"

func TestCountBits(t *testing.T) {

    if CountBits(0) != 0 {
        t.Error("Expected 0")
    }

    if CountBits(-1) != 0 {
        t.Error("Expected 0")
    }

    if CountBits(15) != 4 {
        t.Error("Expected 4")
    }

    if CountBits(15333333333442434) != 34 {
        t.Error("Expected 34")
    }
}

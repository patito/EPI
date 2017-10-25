package main

import "testing"

func TestCountBits(t *testing.T) {

    if res := CountBits(0); res != 0 {
        t.Errorf("Expected 0 Received %d", res)
    }

    if res := CountBits(-1); res != 0 {
        t.Errorf("Expected 0 Received %d", res)
    }

    if res := CountBits(15); res != 4 {
        t.Errorf("Expected 4 Received %d", res)
    }

    if res := CountBits(15333333333442434); res != 34 {
        t.Errorf("Expected 34 Received %d", res)
    }
}

package misc_test

import (
	"fmt"
	"testing"

	"github.com/patito/EPI/misc/missing_integer/go"
)

func TestShouldGetMissingIntegerCorrectly(t *testing.T) {
	type test struct {
		Want   int
		Values []int
	}
	cases := []test{
		test{Values: []int{1, 3, 6, 4, 1, 2}, Want: 5},
		test{Values: []int{1, 2, 3}, Want: 4},
		test{Values: []int{-1, -3}, Want: 1},
	}

	for i, c := range cases {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			if got := misc.Solution(c.Values, len(c.Values)); got != c.Want {
				t.Errorf("Want: %d but got %d", c.Want, got)
			}
		})
	}

}

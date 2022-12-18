func numJewelsInStones(J string, S string) int {
	output := 0
	for x:=0; x<len(J); x++ {
		for y:=0; y<len(S); y++ {
			if(J[x] == S[y]){
				output++
			}
		}
	}
	return output
}
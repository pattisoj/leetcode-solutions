/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @return {boolean}
 */
var validPath = function(n, edges, start, end) {
	if (start === end) return true;

	const record = [...Array(n)].map((_, index) => index);
	const find = (vertex) => {
		return record[vertex] == vertex 
			? vertex 
			: record[vertex] = find(record[vertex]);
	};

	for (const path of edges) {
		if (path.includes(start) && path.includes(end)) return true;
		const [u, v] = path;

		record[find(u)] = record[find(v)];
	}

	return find(start) === find(end);
};
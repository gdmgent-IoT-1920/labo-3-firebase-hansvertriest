for(let box = 0; box < 64; box ++) {
	const row = Math.floor(box / 8);
	const column = box % 8;
	console.log(document.getElementById('matrix-form'));
	console.log(`pixel-${row}-${column}`);
	const checkbox = document.getElementById(`pixel-${row}-${column}`);
	console.log(checkbox);
	checkbox.onchange((event) => {
		console.log(event.target);
	});
}
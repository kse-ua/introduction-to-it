function move(offsetPoint, initialPoints) {
    let results = [];
    for (let element of initialPoints) {
        if (typeof element === 'object') {
            element.x += offsetPoint.x;
            element.y += offsetPoint.y;
            results.push(element);
        } else {
            let parsed = JSON.parse(element);
            parsed.x += offsetPoint.x;
            parsed.y += offsetPoint.y;
            results.push(parsed);
        }
    }
    return results;
}

const polyline = [
    { x: 0, y: 0 },
    { x: 10, y: 10 },
    '{ "x": 20, "y": 20 }',
    { x: 30, y: 30 },
];

console.log(move({ x: 10, y: -5 }, polyline))

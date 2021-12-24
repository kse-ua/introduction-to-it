'use strict';

class Offset {
    constructor(displace) {
        this.displace = displace;
    }

    shift(coord) {
        return {
            x: coord.x + this.displace.dx,
            y: coord.y + this.displace.dy
        };
    }
}

const parsers = {
    string: JSON.parse,
    object: (obj) => obj,
};

const parse = (item) => {
    const parser = parsers[typeof item];
    return parser(item);
};

const polyline = [
    { x: 0, y: 0 },
    { x: 10, y: 10 },
    '{ "x": 20, "y": 20 }',
    { x: 30, y: 30 },
];

const offset = new Offset({ dx: 10, dy: -5 });
const path = polyline.map(parse).map((coord) => offset.shift(coord));
console.log({ path });

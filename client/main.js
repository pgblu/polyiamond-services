'use strict';

const SIZE = 30;
const GRIDOFFSETX = SIZE;
const GRIDOFFSETY = SIZE;
const RATIO = 1.73205;

const VERTEX_NAMES = [
'vertex', 'base-left', 'base-right'
];

function GridPoint(x, y) {
  this.x = GRIDOFFSETX + x;
  this.y = GRIDOFFSETY + y;
}

function setValues(obj) {
  for (let i = 0; i <= 7; i++) {
    for (let j = 0; j <= 7; j++) {
      const ROWOFFSET = SIZE * (i % 2);
      let x = SIZE * j + ROWOFFSET;
      let y = SIZE * RATIO * i;
      obj.push(new GridPoint(x,y));
    }
  }
};

function Moniamond(gridPoint, orientation) {
  this.left = gridPoint.x + "px";
  this.top = gridPoint.y + "px";
  this.orientation = orientation;
  this.node = undefined;
  this.vertexClass = undefined;
}

Moniamond.prototype.render = function(aNode) {
  this.node = '.' + aNode;
  $(this.node).css({
    'left': this.left,
    'top': this.top,
  }).addClass('triangle-' + this.orientation);
}

Moniamond.prototype.rotate = function(vertexName) {
  if (this.node != undefined) {
    this.vertexClass = 'axis-' + vertexName + '-' + this.orientation;
    $(this.node).addClass(this.vertexClass);
  }
}

Moniamond.prototype.clear = function() {
  if (this.node != undefined) {
    $(this.node).removeClass(this.vertexClass);
  }
}

function Polyiamond() {

}

$(document).ready(function() {
  let myGridPoints = new Array();
  setValues(myGridPoints);
  let tgl1 = new Moniamond(myGridPoints[1],'down');
  tgl1.render('tgl-1');
  let tgl2 = new Moniamond(myGridPoints[2],'up');
  tgl2.render('tgl-2');
  let tgl3 = new Moniamond(myGridPoints[9],'down');
  tgl3.render('tgl-3');
  tgl2.rotate(VERTEX_NAMES[0]);
  tgl3.rotate(VERTEX_NAMES[2]);
});

//compose static triangles
//add mobile triangles
//move mobile triangle
//replace mobile triangle with new positional data
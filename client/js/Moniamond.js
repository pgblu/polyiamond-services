'use strict';

export class Moniamond {
  constructor(gridPoint, orientation) {
    this.left = gridPoint.x + 'px';
    this.top = gridPoint.y + 'px';
    this.orientation = orientation;
    this.node = undefined;
    this.vertexClass = undefined;
  }

  setNode = (myNode) => {
    this.node = myNode;
  }

  let render = (myNode) => {
    setNode('.' + myNode);
    $(this.node).css({
      'left': this.left,
      'top': this.top,
    }).addClass('triangle-' + this.orientation);
  }
}
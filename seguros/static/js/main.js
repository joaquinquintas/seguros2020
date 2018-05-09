function aload(nodes) {
  'use strict';

  var attribute = 'data-aload';

  nodes = nodes || window.document.querySelectorAll('[' + attribute + ']');

  if (nodes.length === undefined) {
    nodes = [nodes];
  }

  [].forEach.call(nodes, function (node) {
    node[ node.tagName !== 'LINK' ? 'src' : 'href' ] = node.getAttribute(attribute);
    node.removeAttribute(attribute);
  });

  return nodes;
}

function introLoader(element,delay) {
    this.open = function(callback) {
      setTimeout(function() {
        $(element).fadeIn(500, function() {
          if(callback !== undefined) callback();
        });
      }, delay);
      
    };
    this.close = function(callback) {
      setTimeout(function() {
        $(element).fadeOut(500, function() {
          if(callback !== undefined) callback();
        });
      }, delay);
    };
  }
  var LOADER = new introLoader('#introLoader',500);
  $(window).on('load', function() {
    LOADER.close(function() {
    });
  });


$(document).ready(function () {

    //menu-desktop
    $('#toggle-menu').click(function () {
        $(this).toggleClass('menu-opened');
        $('#menu').toggleClass('animated fadeIn');
        $('#menu').toggleClass('dn');
    });

        //menu-mobile
        $('#sidebar-m').click(function () {
          $(this).toggleClass('rotate-m');
          $('.sidebar-data').toggleClass('active-side');
      });
//dropdown
      $('.dropdown-menu').click(function() {
        $(this).closest('.menu-drop').find('list-drop').toggleClass('animated fadeIn');
    });
  
});


window.onload = () => {
    aload();
};



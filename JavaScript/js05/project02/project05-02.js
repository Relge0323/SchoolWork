"use strict";
/*    JavaScript 7th Edition
      Chapter 5
      Project 05-02

      Project to move images between a photo bucket and photo list.
      Author: Michael Egler
      Date:   03/26/2025

      Filename: project05-02.js
*/

let images = document.getElementsByTagName("img");
let photoBucket = document.getElementById("photo_bucket");
let photoList = document.getElementById("photo_list");

// for loop going thru image collection
for (let i = 0; i < images.length; i++) {
      images[i].onclick = function() {
            // is the image in the bucket?
            if (this.parentElement.id === "photo_bucket") {
                  let newItem = document.createElement("li");

                  photoList.appendChild(newItem);

                  newItem.appendChild(this);
            } else {
                  let oldItem = this.parentElement;

                  photoBucket.appendChild(this);

                  oldItem.parentElement.removeChild(oldItem);
            }
      };
}
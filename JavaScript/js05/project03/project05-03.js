"use strict";
/*    JavaScript 7th Edition
      Chapter 5
      Project 05-03

      Project to create a table of headings from an article
      Author: Michael Egler
      Date:   03/26/2025

      Filename: project05-03.js
*/

let sourceDoc = document.getElementById("source_doc");
let toc = document.getElementById("toc");
let headingCount = 1;
const heading = "H2";

for (let i = sourceDoc.firstElementChild; i !== null; i = i.nextElementSibling) {
    if (i.nodeName === heading) {
        let anchor = document.createElement("a");

        anchor.setAttribute("name", "doclink" + headingCount);

        i.insertBefore(anchor, i.firstChild);

        let listItem = document.createElement("li");

        let link = document.createElement("a");

        listItem.appendChild(link);

        link.textContent = i.textContent;

        link.setAttribute("href", "#doclink" + headingCount);

        toc.appendChild(listItem);

        headingCount++;
    }
}
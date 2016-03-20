/*  anataxCodelettes.js
		bubBA scripter and java drinker
		created 040315 (as bibcode.js)
		last modified 050309

		contains javascript functions for the 
		Anatomy & Taxonomy of Protein Structure
		redo on the kinemage website
contains functions:
	blankOpener - allows functionality of the old <a> tag open href: in blank window
	refGetter - biblio lookup and display
*/

function blankOpener()  {
	if (!document.getElementsByTagName) return;
	var anchors = document.getElementsByTagName("a");
	for (var i=0; i < anchors.length; i++) { 
		var anchor = anchors[i];
		if (anchor.getAttribute("href") &&
				anchor.getAttribute("rel") == "nuwin")
			anchor.target = "_blank";
	}
}

function refgetter(refID)  {
	var refID
	window.open("anatax.ref.html#"+ refID,"AnataxBibliography","width=600,height=200,scrollbar=1")
}

function uprefgetter(refID)  {
	var refID
	window.open('anatax.updateref.html#'+ refID,'AnataxBibliography','width=600,height=200')
}


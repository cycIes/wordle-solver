This is a tool to help wordle players guess words. As they play, when the user inputs information of their attempts, the tool narrows down and generates a ranked list of possible words to guess. <br/>
Credit to dracos for their list of valid wordle words: https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93. <br/>

### Instructions
<ol>
<li>Run main.py to use the wordle guess provider.</li>
<em>Example wordle answer: blimp</em>
<li>The first thing the guesser asks the user to provide is the known letters in the correct position (green letters).</li>
<em>Ex: if the user guessed "stick", they should type "__i\__"</em>
<li>The second thing the guesser asks for is the known letters not in the correct position (yellow letters).</li>
<em>Ex: if the user guessed "plain", they should type "p\__i\_"</em>
<li>The last thing he guesser asks for is the letters revealed to not be in the answer (gray letters).</li>
<em>Ex: if the user guessed "happy", they should type "hay" (notice how "p" was not included because that letter is in the word)</em>
</ol>

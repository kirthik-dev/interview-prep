// Validate before/after-print state transitions without invoking an OS print dialog.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const cards = Array.from({length:97}, (_,i) => ({open:i%4===0,hidden:i%3===0,textContent:'Question',closest:()=>({querySelector:()=>({textContent:'Chapter'})})}));
const chapters = [{hidden:true,querySelector:()=>cards[0]},{hidden:false,querySelector:()=>cards[1]}];
const nodes = new Map();
const element = id => {
  if (!nodes.has(id)) nodes.set(id,{value:'',hidden:false,addEventListener(){},classList:{add(){},remove(){}},focus(){}});
  return nodes.get(id);
};
const events = {};
const sandbox = {
  document:{querySelectorAll(selector){return selector==='.qa'?cards:selector==='.chapter'?chapters:[];},querySelector:element,getElementById(){return null;}},
  window:{addEventListener(name,fn){events[name]=fn;}},
  location:{hash:''},navigator:{},setTimeout,clearTimeout,requestAnimationFrame:fn=>fn()
};
vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname,'..','app.js'),'utf8'),sandbox);
const before = JSON.stringify({cards:cards.map(({open,hidden})=>({open,hidden})),chapters:chapters.map(x=>x.hidden)});
events.beforeprint();
assert(cards.every(c=>c.open&&!c.hidden),'Print must include every answer, including search-hidden answers');
assert(chapters.every(c=>!c.hidden),'Print must include every chapter');
events.beforeprint(); // repeated event must not replace the saved original state
events.afterprint();
assert.equal(JSON.stringify({cards:cards.map(({open,hidden})=>({open,hidden})),chapters:chapters.map(x=>x.hidden)}),before);
events.afterprint();
console.log('PASS: print expands all 97 answers, removes search hiding, and restores original state, including repeated print events.');

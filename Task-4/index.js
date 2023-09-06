const note= {
    'w': './sounds/crash.mp3',

    'a': './sounds/tom-2.mp3',
    
    's':'./sounds/kick-bass.mp3',
    
    'd': './sounds/tom-3.mp3',
    
    'j': './sounds/tom-4.mp3',
    
    'k': './sounds/snare.mp3',
    
    'l':  './sounds/tom-1.mp3'
   
  };
  
  function playNote(key) {
    const audio = new Audio(note[key]);
    audio.play();
  }
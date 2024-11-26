const slides = document.querySelectorAll(".slides img");
let slideIndex = 0;
let intervalId = null;
function initializeSlider(){
  slides[slideIndex].classList.add("displaySlide");
  console.log("hello world");
}
function showSlide(index){
  slides.forEach(slide => {
    slide.classList.remove("displaySlide");
  });
  slides.[slideIndex].classList.add("displaySlide");

}
function prevslide(){

}
function nextslide(){
  slideIndex++;
  showSlide(slideIndex);
}

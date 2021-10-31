var elements = document.querySelectorAll('.item img')

for(var i=0;i< elements.length;i++){
    elements[i].addEventListener('click',function(){
        console.log(sphere.material)
        sphere.material.map=THREE.ImageUtils.loadTexture(this.getAttribute('src'))
        sphere.material.map.repeat.x = -1
        sphere.material.map.wrapS = THREE.RepeatWrapping
        sphere.material.needsUpdate = true;
    })
}


const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(-1, 0, 0);

const geometry = new THREE.SphereGeometry(50, 32, 32);
const textureLoader = new THREE.TextureLoader()
var element = document.querySelector('.item img')
var lien = element.getAttribute('src')
const texture = textureLoader.load(lien)
texture.wrapS = THREE.RepeatWrapping
texture.repeat.x = -1
var material = new THREE.MeshBasicMaterial({
    map: texture,
    side: THREE.DoubleSide
});
const sphere = new THREE.Mesh(geometry, material);
scene.add(sphere);

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const controls = new OrbitControls(camera, renderer.domElement);
controls.rotateSpeed = 0.2
controls.enableZoom = true;
controls.minDistance = 0;
controls.maxDistance = 10;
controls.update();

function animate() {
    requestAnimationFrame(animate)
    renderer.render(scene, camera)
}

animate()

function onResize() {
    renderer.setSize(window.innerWidth, window.innerHeight)
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
}

window.addEventListener('resize', onResize)




$('.owl-carousel').owlCarousel({
    loop: true,
    margin: 10,
    nav: false,
    dots: true,
    responsive: {
        0: {
            items: 2
        },
        600: {
            items: 5
        },
        1000: {
            items: 7
        }
    }
})

var images = document.querySelectorAll('.btn img')
for(var i=0;i< images.length;i++){
    images[i].addEventListener('click',function(){
        image = document.querySelector('.invisible')
        image.classList.remove("invisible")
        this.classList.add("invisible")
        carouel = document.querySelector('.carousel')
        if (carouel.classList.contains('invisible')){
            carouel.classList.remove('invisible')
        }else{
            carouel.classList.add('invisible')
        }
    })
}
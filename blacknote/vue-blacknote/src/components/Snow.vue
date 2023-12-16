<!--Snow.vue-->
<template>
  <div id="main" style="z-index: 1;">
    <canvas id="canvas" ref="canvas" style="position: fixed; top: 0; width: 100%; height: 100%;"></canvas>
  </div>
</template>

<script>
export default {
  data() {
    return {
      canvas: null,
      ctx: null,
      W: 0,
      H: 0,
      mp: 500,
      particles: [],
      t: 0,
    };
  },
  mounted() {
    this.initCanvas();
    this.draw();
  },
  methods: {
    initCanvas() {
      this.canvas = this.$refs.canvas;
      this.ctx = this.canvas.getContext("2d");

      this.W = window.innerWidth;
      this.H = window.innerHeight;
      this.canvas.width = this.W;
      this.canvas.height = this.H;

      this.mp = 500;
      this.particles = [];
      for (let i = 0; i < this.mp; i++) {
        this.particles.push({
          x: Math.random() * this.W, // x坐标
          y: Math.random() * this.H, // y坐标
          r: Math.random() * 2 + 1, // 半径
          d: Math.random() * this.mp, // 密度
          size: Math.random() * 5 + 1, // 1到10之间的大小属性
        });
      }
    },
    draw() {
      this.ctx.clearRect(0, 0, this.W, this.H);

      for (let i = 0; i < this.mp; i++) {
        const p = this.particles[i];

        this.ctx.fillStyle = "rgba(230, 230, 230, 0.8)";
        this.ctx.beginPath();
        this.ctx.moveTo(p.x, p.y);
        this.ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2, true); // 使用p.size作为大小
        this.ctx.fill();
      }

      this.update();
      requestAnimationFrame(this.draw);
    },
    update() {
      this.t += 0.01;

      for (let i = 0; i < this.mp; i++) {
        const p = this.particles[i];

        p.y += Math.cos(this.t + p.d) + 1 + p.size / 2;
        p.x += Math.sin(this.t) * 2;

        if (p.x > this.W || p.x < 0 || p.y > this.H) {
          if (Math.sin(this.t) > 0) {
            this.particles[i] = {
              x: Math.random() * this.W,
              y: -10,
              r: p.size, // 更新大小属性
              d: p.d,
              size: p.size,
            };
          } else {
            this.particles[i] = {
              x: this.W + 10,
              y: Math.random() * this.H,
              r: p.size, // 更新大小属性
              d: p.d,
              size: p.size,
            };
          }
        }
      }
    },
  },
};
</script>

<style>
#main {
  margin: 0;
  padding: 0;
  z-index: 999;
  background-repeat: no-repeat;
  position: absolute;
  background-size: 100% 100%;
  overflow: hidden;
}

canvas {
  display: block;
}
</style>

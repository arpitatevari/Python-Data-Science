<!DOCTYPE html>
<html>
  <head>
    <style>
      #canvas {
        border: 1px solid black;
      }
    </style>
  </head>
  <body>
    <canvas id="canvas" width="500" height="500"></canvas>
    <script>
      const canvas = document.getElementById("canvas");
      const ctx = canvas.getContext("2d");
      const colors = ["red", "blue", "green", "yellow"];
      const x = 50;
      const y = 50;
      const radius = 40;

      for (let i = 0; i < 4; i++) {
        drawCircle(x, y + i * 100, colors[i]);
        drawArrow(x + radius, y + i * 100);
      }

      function drawCircle(x, y, color) {
        ctx.beginPath();
        ctx.arc(x, y, radius, 0, 2 * Math.PI);
        ctx.fillStyle = color;
        ctx.fill();
        ctx.stroke();
      }

      function drawArrow(x, y) {
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(400, y);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(390, y - 10);
        ctx.lineTo(400, y);
        ctx.lineTo(390, y + 10);
        ctx.stroke();
      }
    </script>
  </body>
</html>
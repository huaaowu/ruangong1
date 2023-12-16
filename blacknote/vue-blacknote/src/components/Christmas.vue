<template>
</template>

<script>
import customCursorImage from '../images/Christ.png'; // 替换成你的图片路径

export default {
  data() {
    return {
      customCursor: `url(${customCursorImage}), auto`
    };
  },
  mounted() {
    // 在页面加载后，将鼠标样式设置为自定义图片，通过setTimeout来延迟执行
    setTimeout(() => {
      document.body.style.cursor = this.customCursor;
    }, 10000); // 100毫秒延迟，你可以根据实际情况调整
  },
};
</script>

<style scoped>
/* 可以在这里添加组件的样式，例如设置鼠标样式的位置 */
</style>

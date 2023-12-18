<template>
  <div class="three-equal-parts">
    <!-- 第一个部分 -->
    <div class="part">
      <div class="image-container">
        <img src="../images/image1.png" alt="Image 1" />
      </div>
      <strong class="bold-text">如何进行高光谱图像的分类？</strong>
      <p class="smaller-text">
        使用我们简单的工具，您只需上传您的图片文件(.mat格式),然后这些图片将会在几秒钟内自动分类成一个单独的PNG文件。
      </p>
    </div>

    <!-- 第二个部分 -->
    <div class="part">
      <div class="image-container">
        <img src="../images/image2.png" alt="Image 2" />
      </div>
      <strong class="bold-text">支持.mat的输入格式</strong>
      <p class="smaller-text">你可以直接通过上传该文件，即可以进行分类</p>
    </div>

    <!-- 第三个部分 -->
    <div class="part">
      <div class="image-container">
        <img src="../images/image3.png" alt="Image 3" />
      </div>
      <strong class="bold-text">100%安全</strong>
      <p class="smaller-text">
        您所有上传到我们服务器的.mat文件以及我们分类之后的图片将会被立即删除。我们不会保存您的任何图片。
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dowm',
};
</script>

<style scoped>
.three-equal-parts {
  margin-top: 20%;
  margin: 0 auto;
  display: flex;
  width: 80%;
}

.part {
  flex: 1;
  width: 20%;
  padding: 10px;
  box-sizing: border-box;
  text-align: center;
  margin: 0 5px;
}

.image-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

img {
  margin-top: 20%;
  margin-bottom: 2%;
  width: 5%; 
  height: auto;
}

.bold-text {
  font-weight: bold;
  margin: 10px 0;
}

.smaller-text {
  font-size: 0.9em; 
  color: #666;
  word-wrap: break-word;
  max-width: 100%;
}
</style>

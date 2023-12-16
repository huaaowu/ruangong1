<template>
 
  <Navbar></Navbar>
  <Christmas></Christmas>
   <Snow></Snow>
  <section v-if="!begincat" class="index_content" >
    <div class="function_box" id="choosefile">
      <div class="function_choosefile" style="border-bottom: 0;">
        <input type="hidden" id="id" name="id" value="20170902001">
        <div class="function_choosefile_input">
          <div class="canvas_container" id="container">
            <div class="canvas_box">
              <canvas id="the-canvas" class="canvas_img" style="width:112px;height:145px;"></canvas>
              <div class="canvas_title"></div>
              <a class="canvas_delete"><img src="./images/canvas_delete.png" alt="canvas delete" /></a>
            </div>
          </div>
          <div class="input_box" id="chooseInput" style="z-index: 1;" v-show="!showConversionButton"  >
            <span><label for="openImage">选择图片</label></span>
            <input type="file" id="openImage" accept="image/*" name="files" @change="handleFileChange" />
          </div>
          <div class="input_box" id="startConversion" v-show="showConversionButton">
            <button type="button" class="input_box_conversion" @click="changeImage">{{ ShowTitle }}</button>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- 显示分类之后的图片 -->
  <div style="display: flex; flex-direction: row;" v-if="begincat">
    <div class="container ">
      <div class="text-style">原图</div>
      <img :src="imageURLY" alt="原图" class="image" style="width:100%">
    </div>
    <div class="container ">
      <div class="text-style">分类结果</div>
      <img v-if="!imageURL" src="./images/loading2.gif" alt="正在加载中" class="image" style="width: 100%;">
      <img v-else="imageURL" :src="imageURL" alt="分类结果" class="image" style="width:100%">
      <div v-if="imageURL" class="middle">
        <div class="text"> <a :href="imageURL">下载图片</a></div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';
import Snow from './components/Snow.vue';
import Christmas from './components/Christmas.vue';
import axios from 'axios';


export default {
  components: {
    Navbar,
    Christmas,
    Snow
},
  data() {
    return {
      showConversionButton: false,
      uploadedFile: null,
      imageURL: null,
      ShowTitle: "开始分类",
      imageURLY:null,
      begincat :false,
    };
  },
  methods: {
    handleFileChange(event) {
      const fileInput = event.target;
      const file = fileInput.files[0];
      if (file) {
        const fileName = file.name;
        const fileSize = file.size;
        console.log(`选择的文件: ${fileName}, 大小: ${fileSize} 字节`);
        // 使用FileReader读取文件
        const reader = new FileReader();
        reader.onload = (e) => {
          const imageDataURL = e.target.result;
          console.log('图像的 Data URL:', imageDataURL);
          this.imageURLY = imageDataURL
        };
        // 以 Data URL 格式读取文件
        reader.readAsDataURL(file);
        this.showConversionButton = true
        this.uploadFile();
      }
    },
    //上传文件                                                                    
    uploadFile(file) {
      const formData = new FormData();
      formData.append('files', file);
      // 使用 Axios 将文件上传到服务器
      axios.post('http://127.0.0.1:8080/upload', formData)
        .then(response => {
          console.log('文件上传成功:', response.data);
          this.showConversionButton = true;

        })
        .catch(error => {
          console.error('上传文件时发生错误:', error);
          // 处理错误
        });
    },
    //点击分类，返回链接
    changeImage() {
      this.begincat = true
      const url = 'http://127.0.0.1:8080/change';
      axios.get(url)
        .then(response => {
          this.imageURL = response.data
          this.ShowTitle = "分类完成"
          
        })
        .catch(error => {
          console.error('加载图片时发生错误:', error);
        });
    },
  },
};
</script>

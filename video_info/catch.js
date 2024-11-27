document.addEventListener("DOMContentLoaded", function() {
    const movieInput = document.getElementById('movie-name');
    const movieList = document.getElementById('movie-list');
    const urlList = document.getElementById('url-list');
    const grabButton = document.getElementById('grab-video');
    const videoFolder = document.getElementById('video-folder');

    let selectedMovie = '';
    let selectedUrl = '';

    // 监听影视剧名称的输入，进行模糊查询
    movieInput.addEventListener('input', function() {
        const query = movieInput.value.trim();
        if (query.length > 0) {
            fetch(`/search_movie?name=${query}`)
                .then(response => response.json())
                .then(data => {
                    movieList.innerHTML = '';
                    movieList.style.display = 'block';
                    data.movies.forEach(movie => {
                        const div = document.createElement('div');
                        div.textContent = movie;
                        div.onclick = () => selectMovie(movie);
                        movieList.appendChild(div);
                    });
                });
        } else {
            movieList.style.display = 'none';
        }
    });

    // 选择影视剧
    function selectMovie(movie) {
        selectedMovie = movie;
        movieInput.value = movie;
        movieList.style.display = 'none';

        // 根据影视剧名称请求视频URL列表
        fetch(`/get_video_urls?movie=${movie}`)
            .then(response => response.json())
            .then(data => {
                urlList.innerHTML = '';
                urlList.style.display = 'block';
                data.urls.forEach(url => {
                    const div = document.createElement('div');
                    div.textContent = url;
                    div.onclick = () => selectUrl(url);
                    urlList.appendChild(div);
                });
            });
    }

    // 选择视频URL
    function selectUrl(url) {
        selectedUrl = url;
        urlList.style.display = 'none';
    }

    // 点击抓取视频按钮
    grabButton.addEventListener('click', function() {
        if (selectedMovie && selectedUrl) {
            fetch(`/download_video?url=${selectedUrl}`)
                .then(response => response.json())
                .then(data => {
                    alert('视频抓取并下载成功！');
                    loadVideoFolder();
                })
                .catch(error => {
                    alert('抓取视频失败！');
                });
        } else {
            alert('请先选择影视剧和视频URL');
        }
    });

    // 加载视频文件夹中的所有视频
    function loadVideoFolder() {
        fetch('/get_video_folder')
            .then(response => response.json())
            .then(data => {
                videoFolder.innerHTML = '';
                data.videos.forEach(video => {
                    const div = document.createElement('div');
                    div.textContent = video;
                    videoFolder.appendChild(div);
                });
            });
    }

    // 页面加载时先显示文件夹内容
    loadVideoFolder();
});

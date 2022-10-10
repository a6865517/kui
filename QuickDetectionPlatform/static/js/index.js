// let imgs = {
//     "test": "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpic1.win4000.com%2Fwallpaper%2F2020-09-24%2F5f6c3d719d393.jpg&refer=http%3A%2F%2Fpic1.win4000.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1659188200&t=ce3e027ff6f2e47a06e98fc6308b4cfc",
//     "staging":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farticle%2Fee175bf8a55ecdf25a147c99c8fd028fbbe7f882.jpg&refer=http%3A%2F%2Fi0.hdslb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1659187031&t=a8b71e72df00844810373657701cce27"
// }
//
let url = 'http://192.168.120.18:8001/'
    // 检测环境  默认为测试环境
let ENV = "test"
    // 检测环境展示文案
const envJson = {
        "test": '测试环境',
        "staging": '预发布环境'
    }
    // baseUrl
const urls = {
    "test": url + 'test/',
    "staging": url + 'sta/',
}


// 检测类型   0金标仪 1血常规  2联测
let checkType = 0
    // 选中试纸
let paperCode = null
    // 选中联测类型
let translocationType = null

// 环境切换
const onChangeEnv = (env) => {
    if (env === ENV) return
    ENV = env
    $('#envButton').text(envJson[env])
        // $('body').css("background",`url(${imgs[env]})`)
}

const numberVal = (value) => {
    // 只保留用户输入的Number字符
    value = value.replace(/[^\d]/g, "");
    value = value.replace(/^0*(0\[1-9])/, "$1");
    value = value.replace(/[^\d]/g, "");
    return value === "" ? "" : Number(value);
};

// 检测类型切换
const onChangeType = (i) => {
    if (i === checkType) return
    checkType = i
    document.querySelectorAll('.tab-item').forEach(t => {
        t.classList.remove('activeTab')
    })
    document.querySelectorAll('.tab-item')[i].classList.add('activeTab')
    if (i === 0) {
        document.querySelector('#papers').classList.remove('hide')
        document.querySelector('#modal-blood').classList.add('hide')
        document.querySelector('#translocation').classList.add('hide')
    } else if (i === 2) {
        document.querySelector('#modal-blood').classList.add('hide')
        document.querySelector('#translocation').classList.remove('hide')
        document.querySelector('#papers').classList.add('hide')
    } else {
        document.querySelector('#modal-blood').classList.remove('hide')
        document.querySelector('#papers').classList.add('hide')
        document.querySelector('#translocation').classList.add('hide')
    }
}


// 选择试纸
const onChangePaper = (i) => {
        paperCode = i
        document.querySelectorAll('.paper-item').forEach(t => {
            t.classList.remove('activePaper')
        })
        document.querySelectorAll('.paper-item')[i].classList.add('activePaper')
    }
    // 选择联测
const onChangeTranslocation = (i) => {
    translocationType = i
    document.querySelectorAll('.translocation-item').forEach(t => {
        t.classList.remove('activeTranslocation')
    })
    document.querySelectorAll('.translocation-item')[i].classList.add('activeTranslocation')
}

// 检测类型选择完毕
const modalSubmit = () => {
    if (checkType === 0) {
        // 金标仪
        if (paperCode === null) {
            Alert('请选择检测试纸')
        } else {
            $('#test_type').text(`金标仪-${papersJson[paperCode]}`)
            $('#exampleModal').modal('toggle')
        }
    } else if (checkType === 1) {
        // 血常规
        $('#test_type').text('血常规')
        $('#exampleModal').modal('toggle')
    } else if (checkType === 2) {
        // 联测
        if (translocationType === null) {
            Alert('请选择联测类型')
        } else {
            let TJson = {
                0: '金标仪联测',
                1: "血常规联测"
            }
            $('#test_type').text(`联测-${TJson[translocationType]}`)
            $('#exampleModal').modal('toggle')
        }
    }
    // $('#exampleModal').modal('toggle')
}


// 开始检测
const submit = () => {
    let path = 'gold_check'
    let num = $('#times').val()
    let phone = $('#phone').val()
    console.log(checkType, paperCode);
    if (num < 1) {
        return Alert('填写检测次数')
    };
    if (phone.length < 11) {
        return Alert('手机号码不合法')
    };
    if (checkType === 0 && paperCode === null) {
        return Alert('请选择检测类型')
    };
    let requestArr = []
    for (let i = 0; i < num; i++) {
        requestArr.push(new Promise((resolve, reject) => {
            let formData = new FormData()
            if (checkType === 0) {
                formData.append('paperCode', paperCode)
            } else if (checkType === 1) {
                path = 'blood_check'
            } else if (checkType === 2 & translocationType === 0) {
                path = 'online_gold_check'
            } else if (checkType === 2 & translocationType === 1) {
                path = 'online_blood_check'
            }
            formData.append('phone', phone)
            $.ajax({
                url: urls[ENV] + path,
                type: "POST",
                data: formData,
                contentType: "application/json",
                dataType: "json",
                contentType: false,
                processData: false,
                success: (res) => {
                    resolve(res.msg)
                },
                error: (err) => {
                    reject(err)
                }
            })
        }))
    }
    Loading.show()
    Promise.all(requestArr).then(res => {
        Loading.hide()
        console.log('res>>>', res);
        Alert(res)
    }).catch(err => {
        Loading.hide()
        Alert('检测未全部执行完毕，请重试')
    })

}


// 工具函数
let alertTimes = null
const Alert = (msg = "iyy测试") => {
    if (alertTimes) {
        clearTimeout(alertTimes)
        $('.alert').removeClass('show')
    }
    $('.msg').text(msg)
    $('.alert').addClass('show')
    alertTimes = setTimeout(() => {
        $('.alert').removeClass('show')
    }, 10000)
}

const Loading = {
    show: function() {
        $('.loading').addClass('loadingActive')
    },
    hide: function() {
        $('.loading').removeClass('loadingActive')
    }
}


// 试纸数据
const papersJson = {
    0: "CRP试纸",
    1: "SAA试纸",
    2: "MP-lgM试纸",
    3: "Cpn-lgM试纸",
    4: "MP-Ab试纸",
    5: "EV71试纸",
    6: "CVA16试纸",
    7: "FluA+B试纸",
    8: "HP-lgM-lgG试纸",
    9: "mALb试纸",
    10: "HbA1C试纸",
    11: "CRP+SAA试纸",
}
const nodemailer = require('nodemailer');
const fs = require('fs');

const transporter = nodemailer.createTransport({
  host: 'smtp.gmail.com',
  port: 465,
  secure: true,
  auth: {
    user: 'area51.automated@gmail.com',
    pass: 'xygs vmhg ayrn kwbc',
  },
});

const options = {
  from: 'area51.automated@gmail.com',
  to: ['yash9910340792@gmail.com', 'guptadivya958@gmail.com','nasharma314@gmail.com','rawatsaditya@gmail.com'], 
  subject: 'your image has been found',
  html: `<p>HI!! Please find your image attached below</p><img src="cid:my-image-id" alt="My Image">`,
};

const attachment = {
  filename: 'my-image.jpg',
  path:'/Users/rajeshgupta/Desktop/demo/group.JPG',
  contentType: 'image/jpeg',
  contentId: 'my-image-id',
};

options.attachments = [attachment];

transporter.sendMail(options, function (err, info) {
  if (err) {
    console.log(err);
    return;
  }
  console.log('sent: ' + info.response);
});
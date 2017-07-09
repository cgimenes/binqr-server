package pi.binqr.binqr

import android.os.Environment
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.Log

import java.io.File
import java.io.FileOutputStream

class SaveActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_save)

        //        byte[] file = getIntent().getExtras().getByteArray("file");
        //        saveFile(file);
    }

    private fun saveFile(vararg bytes: ByteArray) {
        val file = File(Environment.getExternalStorageDirectory(), "photo.jpg")

        if (file.exists()) {
            file.delete()
        }

        try {
            val fos = FileOutputStream(file.path)

            fos.write(bytes[0])
            fos.close()
        } catch (e: java.io.IOException) {
            Log.e("PictureDemo", "Exception in photoCallback", e)
        }

    }
}

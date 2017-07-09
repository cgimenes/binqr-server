package pi.binqr.binqr

import android.Manifest
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Bundle
import android.support.v4.app.ActivityCompat
import android.support.v4.content.ContextCompat
import android.support.v7.app.AppCompatActivity
import android.view.KeyEvent
import android.view.View
import android.widget.*
import com.google.zxing.BarcodeFormat
import com.google.zxing.ResultPoint
import com.journeyapps.barcodescanner.*

import java.io.UnsupportedEncodingException
import java.util.*

/**
 * This sample performs continuous scanning, displaying the barcode and source image whenever
 * a barcode is scanned.
 */
class ScanActivity : AppCompatActivity() {
    private var barcodeView: DecoratedBarcodeView? = null
    private var scannedParts: MutableSet<String>? = null

    private val callback = object : BarcodeCallback {
        override fun barcodeResult(result: BarcodeResult) {
            if (result.text == null || scannedParts!!.contains(result.text)) {
                // Prevent duplicate scans
                return
            }

            var rawBytes = ByteArray(0)
            try {
                rawBytes = result.text.toByteArray(charset("ISO-8859-1"))
            } catch (e: UnsupportedEncodingException) {
                e.printStackTrace()
            }

            scannedParts!!.add(result.text)
            if (true) {
                save(rawBytes)
            }
        }


        override fun possibleResultPoints(resultPoints: List<ResultPoint>) {}
    }

    private fun save(vararg bytes: ByteArray) {
        val intent = Intent(this, SaveActivity::class.java)
        intent.putExtra("file", bytes)
        startActivity(intent)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(R.layout.activity_scan)

        checkAndAskForPermissions()

        barcodeView = findViewById(R.id.barcode_scanner) as DecoratedBarcodeView?
        val decoderFactory = DefaultDecoderFactory(EnumSet.of(BarcodeFormat.QR_CODE), null, "ISO-8859-1", false)
        barcodeView!!.barcodeView.decoderFactory = decoderFactory
        barcodeView!!.decodeContinuous(callback)

        scannedParts = HashSet<String>()

        val progress = findViewById(R.id.progress) as LinearLayout?

        for (i in 1..5) {
            val checkBox = CheckBox(this)
            checkBox.text = i.toString()
            checkBox.isClickable = false
            progress!!.addView(checkBox)
        }

        val first_scan_text = findViewById(R.id.first_scan_text) as TextView?
        first_scan_text!!.visibility = View.GONE
    }

    private fun checkAndAskForPermissions() {
        val neededPermissions = arrayOf(Manifest.permission.CAMERA, Manifest.permission.WRITE_EXTERNAL_STORAGE)
        val ungrantedPermissions = neededPermissions.filterTo(HashSet<String>()) { ContextCompat.checkSelfPermission(this, it) != PackageManager.PERMISSION_GRANTED }

        if (ungrantedPermissions.size > 0) {
            ActivityCompat.requestPermissions(this, ungrantedPermissions.toArray(emptyArray()), 0)
        }
    }

    override fun onResume() {
        super.onResume()

        barcodeView!!.resume()
    }

    override fun onPause() {
        super.onPause()

        barcodeView!!.pause()
    }

    override fun onKeyDown(keyCode: Int, event: KeyEvent): Boolean {
        return barcodeView!!.onKeyDown(keyCode, event) || super.onKeyDown(keyCode, event)
    }
}
